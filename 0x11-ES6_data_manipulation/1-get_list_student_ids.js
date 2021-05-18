const getListStudentIds = (listOfStudents) => (listOfStudents && Array.isArray(listOfStudents)
  ? listOfStudents.map((item) => item.id) : []);
export default getListStudentIds;
