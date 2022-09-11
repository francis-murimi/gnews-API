from django.urls import path

from .views import UserCreate, LoginView, UserProfileDetail, UserProfileList, PastorProfileList, PastorProfileDetail, LeaderProfileList, LeaderProfileDetail
from .church_views import AddChurchMembership, ChurchDetail, ChurchMembershipDetail, ChurchMembershipList, DenominationList, ChurchList
from .product_views import BlogDetail, ChurchBlogList, ChurchPastorBlogList, ChurchPastorList, CommentDetail, CommentList, ServiceDetail, ServiceList, TopicDetail, TopicList


app_name = 'apiv1'

urlpatterns = [
    path("user/", UserCreate.as_view(), name="user_create"), # user creation
    path('login/',LoginView.as_view(), name='login'), # login
    #profiles
    path('profile/',UserProfileList.as_view(),name='user_profile_list'), #user profile list
    path('profile/<int:pk>/',UserProfileDetail.as_view(),name='user_profile_detail'), #user profile detail
    path('pastor/',PastorProfileList.as_view(),name='pastor_profile_list'), #pastor profile list
    path('pastor/<int:pk>/',PastorProfileDetail.as_view(),name='pastor_profile_detail'), #pastor profile detail
    path('leader/',LeaderProfileList.as_view(),name='leader_profile_list'), #leader profile list
    path('leader/<int:pk>/',LeaderProfileDetail.as_view(),name='leader_profile_detail'), #leader profile detail
    # church api views
    path('denomination/',DenominationList.as_view(),name='denomination_list'), # denomination list
    path('church/',ChurchList.as_view(),name='church_list'), # church list
    path('church/<int:pk>/',ChurchDetail.as_view(),name='church_detail'), # church details
    path('member/',ChurchMembershipList.as_view(),name='church_membership_list'), # church membership list
    path('member/<int:pk>/',ChurchMembershipDetail.as_view(),name='church_membership_detail'), # church membership detail
    path('church/<int:pk>/member/',AddChurchMembership.as_view(),name='add_church_membership'), # add a church membership
    # product api views
    path('church/<int:pk>/topic/',TopicList.as_view(),name='topic_list'), # topic list of a given church
    path('topic/<int:pk>/',TopicDetail.as_view(), name='topic_detail'), # topic detail
    path('church/<int:pk>/service/',ServiceList.as_view(),name='service_list'), # service list of a given church
    path('service/<int:pk>/',ServiceDetail.as_view(),name='service_detail'), # service detail
    path('church/<int:pk>/pastor/',ChurchPastorList.as_view(),name='church_pastor_list'), # List of pastors in a given church
    path('church/<int:pk>/pastor/<int:id>/',ChurchPastorBlogList.as_view(),name='church_pastor_blog_list'),
    path('church/<int:pk>/blog/',ChurchBlogList.as_view(),name='church_blog_list'), # list of blogs for a given church
    path('blog/<int:pk>/',BlogDetail.as_view(),name='blog_detail'), # blog detail
    path('blog/<int:pk>/comment/',CommentList.as_view(),name='comment_list'), # comments for a specific blog
    path('comment/<int:pk>/',CommentDetail.as_view(),name='comment_detail'), # comment detail
]