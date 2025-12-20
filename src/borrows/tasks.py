from celery import shared_task

@shared_task
def send_borrow_confirmation(borrow_id):
    print(f"Borrow confirmation sent for borrow ID: {borrow_id}")
