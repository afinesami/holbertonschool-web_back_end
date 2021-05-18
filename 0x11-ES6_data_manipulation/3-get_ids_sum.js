const getStudentIdsSum = (list) => list.reduce((total, student) => total + student.id, 0);

export default getStudentIdsSum;
