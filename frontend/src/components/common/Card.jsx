function Card({

children,

className=""

}){

return(

<div

className={

`bg-white

rounded-2xl

shadow-md

hover:shadow-xl

transition

duration-300

border

border-gray-200

p-6

${className}`

}

>

{children}

</div>

);

}

export default Card;