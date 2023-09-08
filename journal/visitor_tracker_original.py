from datetime import datetime, timedelta

def visitor_tracker(request):
    if not request.session.session_key:
        request.session.create()
        session = request.session.session_key

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        date = datetime.now()
        visitors = '/tmp/visitors.html'
        with open(visitors, "a") as f:
            f.write(f"{session}: {date}: {ip}<br>")
        
    
    
    