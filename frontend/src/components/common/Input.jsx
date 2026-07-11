function Input({
  label,
  className = "",
  ...props
}) {
  return (
    <div className="mb-5">

      {label && (
        <label className="block mb-2 font-medium text-slate-700">
          {label}
        </label>
      )}

      <input
        className={`
          w-full
          border
          border-gray-300
          rounded-xl
          px-4
          py-3
          bg-white
          text-slate-800
          placeholder:text-gray-400
          focus:border-blue-500
          focus:ring-4
          focus:ring-blue-100
          outline-none
          transition-all
          duration-300
          ${className}
        `}
        {...props}
      />

    </div>
  );
}

export default Input;