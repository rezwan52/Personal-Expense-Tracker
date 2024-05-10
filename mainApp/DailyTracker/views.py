from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense


def home(request):
    form = ExpenseForm()
    expenses = Expense.objects.all()  # Retrieve all expenses

    return render(request, "home.html", {"form": form, "expenses": expenses})


def submit_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # Retrieve all expenses including the newly added one
                expenses = Expense.objects.all()
                # print(form.data)

                # return render(request, 'home.html', {'form': ExpenseForm(), 'expenses': expenses})
                return redirect("home")
            except Exception as e:
                # Log the error message
                print(e)
                # Render the form again with an error message
                return render(
                    request,
                    "home.html",
                    {
                        "form": form,
                        "error": "An error occurred while saving the expense.",
                    },
                )

    form = ExpenseForm(request.POST)
    expenses = Expense.objects.all()

    return render(request, "submit_expense.html", {"form": form, "expenses": expenses})
