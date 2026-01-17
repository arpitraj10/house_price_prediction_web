import React, { useState } from "react";
import PredictionForm from "../components/PredictionForm";
import ResultCard from "../components/ResultCard";
import FeatureChart from "../components/FeatureChart";
import { predictPrice } from "../services/api";

const Home = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handlePrediction = async (formData) => {
    setLoading(true);
    try {
      const response = await predictPrice(formData);
      setResult(response);
    } catch (error) {
      console.error("Prediction failed", error);
      alert("Failed to fetch prediction");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-blue-600 mb-8">
          House Price Prediction System
        </h1>

        <PredictionForm onSubmit={handlePrediction} />

        {loading && (
          <p className="text-center mt-4 text-gray-600">Predicting price...</p>
        )}

        {result && (
          <>
            <ResultCard prediction={result} />
            <FeatureChart featureImportance={result.feature_importance} />
          </>
        )}
      </div>
    </div>
  );
};

export default Home;
