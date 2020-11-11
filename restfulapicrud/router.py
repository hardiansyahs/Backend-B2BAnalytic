from employeeapi.viewsets import EmployeeViewset
from employeeapi.viewsets import AccountViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('account', AccountViewset)
