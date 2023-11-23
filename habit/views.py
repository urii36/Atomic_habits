from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from permissions import IsOwnerOrReadOnly
from .models import Habit
from .paginations import HabitPagination
from .serializers import HabitSerializer


class HabitListCreateView(generics.ListCreateAPIView):
    """
    Представление для создания и просмотра списка привычек пользователя.
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = HabitPagination

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Автоматически устанавливаем пользователя при создании привычки
        serializer.save(user=self.request.user)


class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Представление для просмотра, обновления и удаления привычки.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Возвращаем только привычки текущего пользователя
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
