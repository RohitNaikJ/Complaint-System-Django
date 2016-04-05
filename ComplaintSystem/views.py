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


def createNewComplaint(request, createComplaint_title, createComplaint_description, creatComplaint_roomNo, createComplaint_origin, createComplaint_levelOfComplaint, createComplaint_category, createComplaint_status_AS, createComplaint_status_RU, createComplaint_username):
    mytitle = createComplaint_title
    mydescription = createComplaint_description
    mydescription = urllib.unquote(mydescription.replace('+', '%20'))
    myroomno = creatComplaint_roomNo
    myorigin = createComplaint_origin
    mylevelOfComplaint = createComplaint_levelOfComplaint
    mycategory = createComplaint_category
    mycreatedDate = timezone.now()
    mystatus_AS = createComplaint_status_AS
    mystatus_RU = createComplaint_status_RU
    createComplaint_lodgedBy = Users.objects.get(username=createComplaint_username)
    mylodgedBy = createComplaint_lodgedBy
    try:
        user = Complaints(title = mytitle, description = mydescription, complaint_roomNo=myroomno, origin = myorigin, levelOfComplaint = mylevelOfComplaint, category = mycategory, createdDate = mycreatedDate, status_AS = mystatus_AS, status_RU = mystatus_RU, lodgedBy = mylodgedBy)
        user.save()
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
            'contact_number': myuser.contactNo,      #
            'working_authority': myuser.authority,   #
            #
            #
            #
            #   Added a few more return attributes
            #
            #
            #
            #
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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
            'worker_name': worker_name,
            'worker_email': worker_email,
            'worker_contact_no': worker_contact_no,
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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
        }
        list_of_comp.append(jsonobject)
    response = {
        'List_of_InstituteResolvedComplaints' : list_of_comp
    }
    return JsonResponse(response)


def get_URIsC(request):
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
        item_createdDate = item_complaint.createdDate
        item_resolvedDate = item_complaint.resolvedDate
        item_status_AS = item_complaint.status_AS
        item_status_RU = item_complaint.status_RU
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


def returnJSON(request):
    shama = {
        "id": "rnd",
        "name": "shama",
        "number": "19",
        "time": "130",
        "status": "true"
    }
    rohit = {
        "id": "rj",
        "name": "rohit",
        "number": "15",
        "time": "130",
        "status": "true"
    }
    pickup = [rohit]
    pickup.append(shama)
    response = {
        'pickup' : pickup
    }
    return JsonResponse(response)
