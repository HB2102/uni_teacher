import React, { useState, useEffect } from 'react';
import { BiLike,BiDislike  } from "react-icons/bi";
import { TbMessageReport } from "react-icons/tb";
import { CgProfile } from "react-icons/cg";
const SingleComment = () => {
    const [likeNumber, setLikeNumber] = useState(0);
    const [dislikeNumber, setDisLikeNumber] = useState(0);
    return (
        <section dir='rtl'  className="py-4 w-4/5 m-auto">
                    
                    <div className="swiper-slide group bg-white border border-solid border-gray-300 rounded-2xl max-sm:max-w-sm max-sm:mx-auto p-6 transition-all duration-500 hover:border-indigo-600">
                               <div className="flex items-center gap-5 mb-5 sm:mb-9">
                                   {/* <img className="rounded-full object-cover" src="https://pagedone.io/asset/uploads/1696229969.png" alt="avatar"> */}
                                   <CgProfile className='w-16 h-16' />
                                   {/* <img
                                   src="https://pagedone.io/asset/uploads/1696229969.png"
                                       alt="avatar"
                                       className="rounded-full object-cover"
                                   /> */}
                                   <div className="grid gap-1">
                                   <div class="flex items-center flex-1  font-bold leading-tight">Noob master
                                        <span class="mr-2 text-xs font-normal text-gray-500">دو هفته قبل</span>
                                    </div>
                                       <span className="text-sm leading-6 text-gray-500">2 weeks ago </span>
                                   </div>
                               </div>
                         
                               <p 
                                   className="text-lg text-gray-700 leading-6 transition-all duration-500 min-h-24 group-hover:text-gray-900">
                                لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد، کتابهای زیادی در شصت و سه درصد گذشته حال و آینده، شناخت فراوان جامعه و متخصصان را می طلبد، تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی، و فرهنگ پیشرو در زبان فارسی ایجاد کرد، در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها، و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی، و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.
                               </p>
                               <div className="flex items-center mb-3 sm:mb-9 gap-5  transition-all duration-500 mt-5">
                                    <button className="flex flex-row gap-1 ">
                                        <span className='pt-1'> {dislikeNumber}</span>
                                        <BiDislike className='w-7 h-7 ' />
                                    </button>
                                    <button className="flex flex-row gap-1">
                                        <span className='pt-2'> {likeNumber}</span>
                                        <BiLike className='w-7 h-7' />   
                                    </button>
                                    <TbMessageReport className='w-7 h-7 ' />
                               </div>
                           </div>
        </section>
    );
};

export default SingleComment;
