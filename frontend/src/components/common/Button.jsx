import clsx from "clsx";

function Button({

children,

variant="primary",

className,

...props

}){

const styles={

primary:

"bg-blue-600 hover:bg-blue-700 text-white",

secondary:

"bg-violet-600 hover:bg-violet-700 text-white",

outline:

"border border-gray-300 hover:bg-gray-100",

danger:

"bg-red-600 hover:bg-red-700 text-white",

success:

"bg-green-600 hover:bg-green-700 text-white",

};

return(

<button

className={clsx(

"px-6 py-3 rounded-xl font-semibold transition shadow",

styles[variant],

className

)}

{...props}

>

{children}

</button>

);

}

export default Button;