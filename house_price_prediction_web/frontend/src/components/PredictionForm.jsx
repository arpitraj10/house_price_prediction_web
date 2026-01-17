export default function PredictionForm({ onSubmit }) {
  const [form, setForm] = useState({});

  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit(form); }}>
      <input placeholder="Living Area" onChange={e => setForm({...form, gr_liv_area: e.target.value})}/>
      <button className="bg-blue-600 text-white p-2">Predict</button>
    </form>
  );
}
