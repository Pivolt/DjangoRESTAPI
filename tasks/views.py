from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login

from .models import Task, TaskHistory
from .serializers import TaskSerializer, HistorySerializer, UserSerializer

@api_view(['GET'])
def home_page(request):
    api_urls = {
        'Get all':'/tasks',
        'Get query':'/tasks/?field=value',
        'Get one/Update/Delete':'tasks/<int:pk>',
        'Get change history':'/history',
        'Get change history(query)':'/history/?field=value',
    }
    return Response(api_urls)

class UserRegistrationView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
register_request = UserRegistrationView.as_view()


class UserLoginView(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
login_request = UserLoginView.as_view()


class TaskList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        tasks = Task.objects.all()
        task_id = self.request.GET.get('id')
        name = self.request.GET.get('name')
        description = self.request.GET.get('description')
        status = self.request.GET.get('status')
        assigned_user = self.request.GET.get('assigned_user')

        if task_id:
            tasks = tasks.filter(id__icontains=task_id)
        if name:
            tasks = tasks.filter(name__icontains=name)
        if description:
            tasks = tasks.filter(description__icontains=description)
        if status:
            tasks = tasks.filter(status__iexact=status)
        if assigned_user:
            tasks = tasks.filter(assigned_user__username__icontains=assigned_user)
            
        return tasks

task_list = TaskList.as_view()


class TaskDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

task_details = TaskDetails.as_view()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history_list(request):
    history = TaskHistory.objects.all()
    task_id = request.GET.get('task')
    name = request.GET.get('name')
    description = request.GET.get('description')
    status = request.GET.get('status')
    assigned_user = request.GET.get('assigned_user')
    timestamp = request.GET.get('timestamp')

    if task_id:
        history = history.filter(task__id__iexact=task_id)
    if name:
        history = history.filter(name__icontains=name)
    if description:
        history = history.filter(description__icontains=description)
    if status:
        history = history.filter(status__iexact=status)
    if assigned_user:
        history = history.filter(assigned_user__username=assigned_user)
    if timestamp:
        history = history.filter(timestamp__icontains=timestamp)

    serializer = HistorySerializer(history, many=True)
    return Response(serializer.data)
