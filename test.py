
class Person():
    def __init__(self, ten, gioitinh, ngaysinh) -> None:
        self.ten = ten
        self.gioitinh = gioitinh
        self.ngaysinh = ngaysinh

    def description_person(self):
        print(
            f"Ten: {self.ten} \nGioi tinh: {self.gioitinh}\nNgay sinh: {self.ngaysinh}")


class Student(Person):
    def __init__(self, ten, gioitinh, ngaysinh, masinhvien, diemtrungbinh, email) -> None:
        super().__init__(ten, gioitinh, ngaysinh)
        self.masinhvien = masinhvien
        self.diemtrungbinh = diemtrungbinh
        self.email = email

    def description_student(self):
        super().description_person()
        print(
            f"Ten: {self.masinhvien} \nGioi tinh: {self.diemtrungbinh}\nNgay sinh: {self.email}")
