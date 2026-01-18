import axios from "axios";

export const predictPrice = async (data) => {
  const res = await axios.post(
    '${import.meta.env.VITE_API_BASE_URL}/predict',
    data
  );
  return res.data;
};

