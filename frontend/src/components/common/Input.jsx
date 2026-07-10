function Input({

label,

...props

}){

return(

<div className="mb-5">

<label

className="block mb-2 font-medium"

>

{label}

</label>

<input

className="

w-full

border

border-gray-300

rounded-xl

px-4

py-3

focus:border-blue-500

focus:ring-2

focus:ring-blue-200

transition

"

{...props}

/>

</div>

);

}

export default Input;