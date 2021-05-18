const updateStudentGradeByCity = (students, city, newGrade) => students
  .filter((student) => student.location === city)
  .map((item) => {
    const newRecord = { ...item };

    const newStudent = newGrade.find((student) => student.studentId === item.id);
    if (newStudent) newRecord.grade = newStudent.grade;
    else newRecord.grade = 'N/A';
    return newRecord;
  });

export default updateStudentGradeByCity;
