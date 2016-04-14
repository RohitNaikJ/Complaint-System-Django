from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    #url(r'^createNewComplaint/(?P<createComplaint_title>[A-Za-z+]+)/(?P<username>[A-Za-z0-9]+)/$', views.testing_createComplaint),
    url(r'^loginUser/(?P<login_username>[A-Za-z0-9.]+)/(?P<login_password>[A-Za-z0-9]+)/$', views.login, name = 'User Login'),
    url(r'^loginAuthority/(?P<login_username>[A-Za-z0-9.]+)/(?P<login_password>[A-Za-z0-9]+)/$', views.loginA, name = 'Authority Login'),
    url(r'^registerNewAuthority/(?P<authority_name>[A-Za-z+]+)/(?P<authority_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/(?P<authority_username>[A-Za-z0-9]+)/(?P<authority_password>[A-Za-z0-9]+)/(?P<authority_type>[A-Za-z]+)/(?P<authority_contactNo>[0-9]+)/$', views.registerNewAuthority, name='Register New Authority'),
    url(r'^getResolved/(?P<auth_id>\d+)/$', views.getResolved, name = 'Get Resolved Complaints'),
    url(r'^getUnresolved/(?P<auth_id>\d+)/$', views.getUnresolved, name='Get Unresolved Complaints'),
    url(r'^createNewComplaint/(?P<createComplaint_title>[A-Za-z+]+)/(?P<createComplaint_description>[A-Za-z0-9+]+)/(?P<creatComplaint_roomNo>[+A-Za-z0-9_-]+)/(?P<createComplaint_origin>[A-Za-z]+)/(?P<createComplaint_levelOfComplaint>[A-Za-z]+)/(?P<createComplaint_category>[A-Za-z]+)/(?P<createComplaint_username>[A-Za-z0-9]+)/$', views.createNewComplaint, name = "Create New Complaint"),
    url(r'^registerNewUser/(?P<register_name>[A-Za-z+]+)/(?P<register_email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/(?P<register_username>[A-Za-z0-9]+)/(?P<register_password>[A-Za-z0-9]+)/(?P<register_userType>[A-Za-z]+)/(?P<register_residence>[A-Za-z]+)/(?P<register_roomNo>[A-Za-z0-9_-]+)/(?P<register_contactNo>[0-9]+)/$', views.registerNewUser, name='Register New User'),
    url(r'^getRIndividualComplaints/(?P<userID>[0-9]+)/$', views.get_RIC, name='Get Resolved Individual Complaints'),
    url(r'^getURIndividualComplaints/(?P<userID>[0-9]+)/$', views.get_URIC, name='Get Unresolved Individual Complaints'),
    url(r'^getRHostelComplaints/(?P<hostel_name>[A-Za-z]+)/$', views.get_RHC, name='Get Resolved Hostel Complaints'),
    url(r'^getURHostelComplaints/(?P<hostel_name>[A-Za-z]+)/$', views.get_URHC, name='Get Unresolved Hostel Complaints'),
    url(r'^getRInstituteComplaints/$', views.get_RIsC, name = 'Get Resolved Institute Level Complaints'),
    url(r'^getURInstituteComplaints/$', views.get_URIsC, name = 'Get Unresolved Institute Level Complaints'),
    url(r'^getComments/(?P<complaintID>\d+)/$', views.returncomments, name='Get comments of the given ID'),
    url(r'^postComment/(?P<userID>\d+)/(?P<complaintID>\d+)/(?P<commentText>[A-Za-z0-9+]+)/$', views.createComment, name = 'Create a new comment'),
    url(r'^resolveComplaint/(?P<complaintID>[0-9]+)/$', views.resolveComplaint, name='Resolve the Complaint'),
    url(r'^upVoteComplaint/(?P<complaintID>\d+)/(?P<vote>(1|0))/$', views.upDownVoteComplaint, name='UpVote or DownVote the Complaint'),
]