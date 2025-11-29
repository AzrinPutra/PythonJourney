#!usr/bin/env python3

class Student:
    def __init__(self, sid=None, deptid=None, **kwargs):
        super().__init__(**kwargs)
        if sid is not None:    
            self.sid = sid
        if deptid is not None:    
            self.deptid = deptid
        
    def get_info(self):
        return f"StudentID:{self.sid} DepartmentID:{self.deptid}"
    
class Faculty:
    def __init__(self, eid=None, deptid=None, **kwargs):
        super().__init__(**kwargs)
        if eid is not None:
            self.eid = eid
        if deptid is not None:
            self.deptid = deptid
        
    def get_info(self):
        return f"EmployeeID:{self.eid} DepartmentID:{self.deptid}"
    
class PhDStudent(Student, Faculty):
    def __init__(self, sid, eid, deptid):
        super().__init__(sid=sid, eid=eid, deptid=deptid)
        
    def get_info(self):
        return f"StudentID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}"