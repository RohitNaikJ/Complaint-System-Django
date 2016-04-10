from django.utils import timezone
import urllib
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ComplaintSystem.models import AuthorityWorker, Users, Complaints

# Create your views here.

def index(request):
    return HttpResponse('Welcome To Complaint System')


def registerNewUser(request, register_name, register_email, register_username, register_password, register_userType, register_residence, register_roomNo, register_contactNo):
    myname = register_name
    myname = urllib.unquote(myname.replace('+', '%20'))
    myemail = register_email
    myusername = register_username
    mypassword = register_password
    mytypeOfUser = register_userType
    mynameOfResidency = register_residence
    myroomNo = register_roomNo
    mycontactNo = register_contactNo
    try:
        user = Users(name = myname, email = myemail, userName = myusername, password = mypassword, typeOfUser = mytypeOfUser, residency = mynameOfResidency, roomNo = myroomNo, contactNo=mycontactNo)
        user.save()
    except Exception:
        response = {'success': False}
    else:
        response = {'success': True}
    finally:
        return JsonResponse(response)


def registerNewAuthority(request, authority_name,authority_email,authority_username, authority_password, authority_type, authority_contactNo):
    myname = authority_name
    myname = urllib.unquote(myname.replace('+', '%20'))
    myemail = authority_email
    myusername = authority_username
    mypassword = authority_password
    mytypeOfUser = authority_type
    mycontactNo = authority_contactNo
    try:
        authority = AuthorityWorker(name = myname, email = myemail, userName = myusername, password = mypassword, type = mytypeOfUser, contactNo=mycontactNo)
        authority.save()
    except Exception:
        response = {'success':False}
        return JsonResponse(response)
    else:
        response = {'success':True}
        return JsonResponse(response)


def createNewComplaint(request, createComplaint_title, createComplaint_description, creatComplaint_roomNo, createComplaint_origin, createComplaint_levelOfComplaint, createComplaint_category, createComplaint_username):
    mytitle = urllib.unquote(createComplaint_title.replace('+', '%20'))
    mydescription = createComplaint_description
    mydescription = urllib.unquote(mydescription.replace('+', '%20'))
    myroomno = creatComplaint_roomNo
    myorigin = createComplaint_origin
    mylevelOfComplaint = createComplaint_levelOfComplaint
    mycategory = createComplaint_category
    createComplaint_lodgedBy = Users.objects.get(userName=createComplaint_username)
    mylodgedBy = createComplaint_lodgedBy
    try:
        complaint = Complaints(title = mytitle, description = mydescription, complaint_roomNo=myroomno, origin = myorigin, levelOfComplaint = mylevelOfComplaint, category = mycategory, lodgedBy = mylodgedBy)
        complaint.save()
    except Exception:
        response = {'success':False}
    else:
        response = {'success':True}
    finally:
        return JsonResponse(response)


def login(request, login_username, login_password):
    if Users.objects.filter(userName=login_username, password=login_password).exists():
        myuser = Users.objects.get(userName=login_username)
        myname = myuser.name
        myemail = myuser.email
        mytypeOfUser = myuser.typeOfUser
        myresidency = myuser.residency
        roomNo = myuser.roomNo
        info = {
            'name': myname,
            'email': myemail,
            'username': login_username,
            'password': login_password,
            'type_of_user': mytypeOfUser,
            'residency': myresidency,
            'room_no': roomNo,
            'primary_id': myuser.id,
            'contact_number': myuser.contactNo,
        }
        response = {
            'success': True,
            'details': info,
        }
    else:
        response = {
            'success': False,
        }
    return JsonResponse(response)


# Resolved Individual Level Complaints based on the given USER ID
def get_RIC(request, userID):
    user = Users.objects.get(id = userID)
    complaints = user.complaints_set.filter(lodgedBy=user, status_RU=True, levelOfComplaint='individualLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        user_name = user.name
        user_email = user.email
        user_username = user.userName
        item_worker = item_complaint.assignedWorker
        worker_name = item_worker.name
        worker_email = item_worker.email
        worker_contact_no = item_worker.contactNo
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': user_name,
            'username':user_username,
            'user_email': user_email,
            'worker_name': worker_name,
            'worker_email': worker_email,
            'worker_contact_no': worker_contact_no,
            'comments': {},
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_IndividualResolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


# Unresolved Individual Level Complaints based on the given USER ID
def get_URIC(request, userID):
    user = Users.objects.get(id = userID)
    complaints = user.complaints_set.filter(lodgedBy=user, status_RU=False, levelOfComplaint='individualLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        user_name = user.name
        user_email = user.email
        user_username = user.userName
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': user_name,
            'username':user_username,
            'user_email': user_email,
            'comments': {},
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_IndividualUnresolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


# Resolved and Unresolved Hostel Level complaints based on the given hostel name. Only applicable to wardens and students
# Not applicable to Faculty, as faculty are assumed to be housed in individual housing
def get_RHC(request, hostel_name):
    complaints = Complaints.objects.filter(status_RU=True, origin=hostel_name, levelOfComplaint='hostelLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        user = item_complaint.lodgedBy
        user_name = user.name
        user_email = user.email
        user_username = user.userName
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': user_name,
            'username':user_username,
            'user_email': user_email,
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_HostelResolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


def get_URHC(request, hostel_name):
    complaints = Complaints.objects.filter(status_RU=False, origin=hostel_name, levelOfComplaint='hostelLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        created_byUser = item_complaint.lodgedBy
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': created_byUser.name,
            'username': created_byUser.userName,
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_HostelUnresolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


# Institute Level Resolved followed by Unresolved Complaints
def get_RIsC(request):
    complaints = Complaints.objects.filter(status_RU=True, levelOfComplaint='instituteLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        created_byUser = item_complaint.lodgedBy
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': created_byUser.name,
            'username': created_byUser.userName,
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_InstituteResolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


def get_URIsC(request):
    complaints = Complaints.objects.filter(status_RU=False, levelOfComplaint='instituteLevel')
    list_of_comp = []
    for item_complaint in complaints:
        item_id = item_complaint.id
        item_title = item_complaint.title
        item_description = item_complaint.description
        item_category = item_complaint.category
        item_roomNo = item_complaint.complaint_roomNo
        item_origin = item_complaint.origin
        item_level = item_complaint.levelOfComplaint
        item_createdDate = item_complaint.createdDate.date()
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
        created_byUser = item_complaint.lodgedBy
        jsonobject = {
            'id': item_id,
            'title': item_title,
            'description': item_description,
            'category': item_category,
            'room_no': item_roomNo,
            'origin': item_origin,
            'level': item_level,
            'date_created': item_createdDate,
            'date_resolved': item_resolvedDate,
            'assigned_or_unassigned': item_status_AS,
            'resolved_or_unresolved': item_status_RU,
            'byname': created_byUser.name,
            'username': created_byUser.userName,
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_InstituteUnresolvedComplaints': list_of_comp
    }
    return JsonResponse(response)


def resolveComplaint(request, complaintID):
    complaint = Complaints.objects.get(id=complaintID)
    complaint.status_RU = True
    complaint.save()
    return JsonResponse({'success': True})


def upDownVoteComplaint(request, complaintID, vote):
    complaint = Complaints.objects.get(id=complaintID)
    complaint.votes += vote
    complaint.save()
    return JsonResponse({'success': True})


def testing_createComplaint(request, createComplaint_title, username):
    myuser = Users.objects.get(userName=username)
    complaint = Complaints(title = createComplaint_title, description = 'This is just description', complaint_roomNo='D73', origin = 'Karakoram', levelOfComplaint = 'instituteLevel', category = 'plumber', lodgedBy = myuser)
    complaint.save()
    return JsonResponse({'success': True})


def returncomments(request, complaintID):
    complaint = Complaints.objects.get(id = complaintID)
    commentsList = []
    for comment in complaint.comments_set.all():
        title = comment.comment_title
        date = comment.comment_date
        creator = comment.comment_by.name
        jsonobject = {
            'title': title,
            'date': date,
            'creator': creator,
        }
        commentsList.append(jsonobject)
    return JsonResponse({
        'list_of_comments': commentsList
    })