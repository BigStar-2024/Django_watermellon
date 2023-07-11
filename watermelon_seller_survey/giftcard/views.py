from django.shortcuts import render, redirect
from .forms import GiftCardForm
from .models import GiftCard
from django.db import transaction


def seller_intake_survey(request):
    if request.method == 'POST':
        form = GiftCardForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            final = request.POST.get('final')

            with transaction.atomic():
                if not request.session.session_key:
                    request.session.create()
                session_id = request.session.session_key

                # Will use session_id for survey_id
                gift_card, created = GiftCard.objects.update_or_create(
                    survey_id=session_id,
                    defaults={**data}
                )

                # Will reset session key then the survey is completed.
                if final:
                    request.session.flush()

            return redirect('intake_survey')
        else:
            print('Form invalid')
    else:
        form = GiftCardForm()
    return render(request, 'form.html', {'form': form})


def seller_intake_survey_list(request):
    giftcards = GiftCard.objects.all()
    for giftcard in giftcards:
        print(giftcard.deposit_or_validate)
    return render(request, 'results.html', {'giftcards': giftcards})