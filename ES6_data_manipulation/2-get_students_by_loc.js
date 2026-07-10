export default function getStudentsByLocation(students){
    return students.filter(student => student.location == "city")
}
