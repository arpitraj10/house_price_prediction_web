import React from "react";

const ResultCard = ({ prediction }) => {
  if (!prediction) return null;

  return (
    <div className="bg-white shadow-lg rounded-xl p-6 mt-6 w-full max-w-xl">
      <h2 className="text-2xl font-semibold text-gray-800 mb-4">
        Prediction Result
      </h2>

      <div className="space-y-3">
        <div className="flex justify-between">
          <span className="text-gray-600">Estimated Price</span>
          <span className="font-bold text-green-600 text-lg">
            ₹ {prediction.predicted_price.toLocaleString()}
          </span>
        </div>

        <div className="flex justify-between">
          <span className="text-gray-600">Confidence Range</span>
          <span className="font-medium text-gray-800">
            ₹ {prediction.confidence_range.min.toLocaleString()} – ₹{" "}
            {prediction.confidence_range.max.toLocaleString()}
          </span>
        </div>
      </div>
    </div>
  );
};

export default ResultCard;
