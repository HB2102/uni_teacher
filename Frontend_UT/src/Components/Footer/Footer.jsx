import { Typography } from "@material-tailwind/react";
import { motion } from 'framer-motion'; 
import { useInView } from 'react-intersection-observer';
import { FaGithub } from 'react-icons/fa';
import {BiLogoGmail , BiLogoTelegram } from "react-icons/bi";
import { useNavigate } from 'react-router-dom';
const LINKS = [
  {
    title: "تماس با ما",
    items: "Request",
  },
  {
    title: "درباره‌ی ما",
    items: "About",
  },
  {
    title: "بلا بلا بلا",
    items: "blah",
  },
];
 
const currentYear = new Date().getFullYear();
 
export function Footer() {
  const navigate = useNavigate();
  const { ref: refFooterSection, inView: inViewFooterSection } = useInView({
    triggerOnce: true, 
    threshold: 0,
  });
 const handleNavigate=(link)=>{
  console.log(link);
  
switch (link) {
    case "Request" :
      navigate('/Request')
      break;
    case "About" :
      navigate('/AboutUs')
      break;
  default:
    break;
}
 }
  return (
    <motion.div 
      ref={refFooterSection}
      initial={{ y: -100, opacity: 0 }} 
      animate={ inViewFooterSection ? { y: 0, opacity: 1 } : { y: -100, opacity: 0 }} 
      transition={{ duration: 1 }} 
    >
      <footer className="relative w-full mt-10 ">
        <div className="mx-auto w-full max-w-full ">
          <div className="grid grid-cols-1 mb-3 justify-between gap-2 md:grid-cols-2">
            <Typography variant="h5" className="">
              فتل بهزادی
            </Typography>
            <div className="grid grid-cols-3 justify-between">
              {LINKS.map(({ title, items }) => (
                <h2 key={title} onClick={() => handleNavigate(items)}>
                  <Typography color="white" className="font-medium opacity-40">
                    {title}
                  </Typography>
                </h2>
              ))}
            </div>
          </div>
          <div className="flex w-full flex-col items-center justify-center border-t border-blue-gray-50 py-4 md:flex-row md:justify-between">
            <Typography
              variant="small"
              className="mb-4 text-center font-normal text-blue-gray-900 md:mb-0"
            >
              &copy; {currentYear} <a href="https://material-tailwind.com/"> فتل بهزادی</a>. All
              Rights Reserved.
            </Typography>
            <div className="flex gap-4 text-blue-gray-900 sm:justify-center">
              <Typography as="a" href="#" className="opacity-80 transition-opacity hover:opacity-100">
                <BiLogoTelegram className="h-8 w-8" />
              </Typography>
              <Typography as="a" href="#" className="opacity-80 transition-opacity hover:opacity-100">
                <BiLogoGmail className="h-8 w-8" />
              </Typography>
              <Typography as="a" href="#" className="opacity-80 transition-opacity hover:opacity-100">
                <FaGithub className="h-8 w-8" />
              </Typography>
            </div>
          </div>
        </div>
      </footer>
    </motion.div>
  );
}

export default Footer;
