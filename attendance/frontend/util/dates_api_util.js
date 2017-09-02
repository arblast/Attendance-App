export const createDate = (dateParams, success, error) => {
  $.ajax({
    type: "POST",
    data: dateParams.params,
    url: "/attendanceapp/date/create",
    headers: {'X-CSRFToken': dateParams.token},
    success,
    error
  });
}

export const fetchDate = (dateParams, success, error) => {
  let year = dateParams.year;
  let month = dateParams.month;
  let day = dateParams.day;
  $.ajax({
    type: "GET",
    url: `/attendanceapp/date/${year}/${month}/${day}`,
    success,
    error
  });
};
