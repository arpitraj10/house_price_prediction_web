import axios from "axios";

export const predictPrice = async (data) => {
  const res = await axios.post("https://your-backend-url/predict", data);
  return res.data;
};
