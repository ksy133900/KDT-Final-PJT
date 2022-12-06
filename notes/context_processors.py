from .models import Notes

def counter(request):
    read_count = 0
    reads = Notes.objects.all().filter(to_user__id=request.user.pk)
    for read_item in reads:
        if read_item.read == 0:
            read_count += 1

    return {"read_count": read_count}