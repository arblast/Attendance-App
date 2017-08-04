export const CREATE_DATE = "CREATE_DATE";
export const FETCH_DATE = "FETCH_DATE";

export const createDate = (dateParams) => ({
  type: CREATE_DATE,
  dateParams
});

export const fetchDate = (dateParams) => ({
  type: FETCH_DATE,
  dateParams
});
