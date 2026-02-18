from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Choice, Submission, Enrollment


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = course.question_set.all()

    if request.method == 'POST':
        enrollment = Enrollment.objects.first()
        submission = Submission.objects.create(enrollment=enrollment)

        selected_ids = request.POST.getlist('choice')

        for choice_id in selected_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)

        return show_exam_result(request, submission.id)

    return render(request, 'onlinecourse/course_details_bootstrap.html', {
        'course': course,
        'questions': questions
    })


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_choices = submission.choices.all()

    total_score = 0
    total_grade = 0

    for question in Question.objects.all():
        total_grade += question.grade
        selected_ids = [choice.id for choice in selected_choices]
        if question.is_get_score(selected_ids):
            total_score += question.grade

    context = {
        'score': total_score,
        'total': total_grade
    }

    return render(request, 'onlinecourse/exam_result.html', context)
