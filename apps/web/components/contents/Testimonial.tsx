'use client'

import Image from 'next/image'
import { useRef } from 'react'
import { FaQuoteLeft, FaArrowLeft, FaArrowRight } from 'react-icons/fa'
import { Swiper, SwiperSlide } from 'swiper/react'
import { Navigation, Autoplay } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/navigation'

export default function Testimonial() {    const prevRef = useRef<HTMLButtonElement | null>(null)
    const nextRef = useRef<HTMLButtonElement | null>(null)

    return (
        <section className="w-full py-16">
            <div className="grid grid-cols-1 lg:grid-cols-2 min-h-[550px]">
                {/* Left Image */}
                <div className="relative overflow-hidden min-h-[550px]">
                    <Image
                        src="/images/testimonial.jpg"
                        alt="Testimonial"
                        fill
                        className="object-cover"
                        priority
                    />
                </div>

                {/* Right Content */}
                <div className="bg-[#222] text-white p-12 lg:p-16 flex flex-col justify-center relative overflow-hidden rounded-br-[35%]">
                    <div className="mb-8">
                        <h5 className="text-orange-500 uppercase tracking-[0.2em] mb-3 font-medium">Testimonial</h5>
                        <h1 className="text-5xl lg:text-6xl font-bold text-gray-200 italic">Our Client Say</h1>
                    </div>

                    <div className="relative">
                        <Swiper
                            modules={[Navigation, Autoplay]}
                            autoplay={{
                                delay: 5000,
                                disableOnInteraction: false,
                            }}
                            loop={true}
                            navigation={{
                                prevEl: prevRef.current,
                                nextEl: nextRef.current,
                            }}                            onSwiper={(swiper) => {
                                // Wait for refs to be defined before initializing navigation
                                if (prevRef.current && nextRef.current) {
                                    // @ts-expect-error: Swiper's type definitions don't fully cover navigation element assignment
                                    swiper.params.navigation.prevEl = prevRef.current
                                    // @ts-expect-error: Swiper's type definitions don't fully cover navigation element assignment
                                    swiper.params.navigation.nextEl = nextRef.current
                                    swiper.navigation.destroy()
                                    swiper.navigation.init()
                                    swiper.navigation.update()
                                }
                            }}
                            className="testimonial-swiper"
                        >
                            {[1, 2].map((_, index) => (
                                <SwiperSlide key={index}>
                                    <div className="mt-6 mb-20">
                                        <p className="text-xl text-gray-300 mb-10 leading-relaxed">
                                            <FaQuoteLeft className="inline-block text-orange-500 mr-3 text-2xl" />
                                            Dolores sed duo clita tempor justo dolor et stet lorem kasd labore dolore lorem ipsum.
                                            At lorem lorem magna ut et, nonumy et labore et tempor diam tempor erat dolor rebum sit ipsum.
                                        </p>
                                        <div className="flex items-center">
                                            <Image
                                                src={`/images/testimonial-${index + 1}.jpg`}
                                                alt="Client"
                                                width={80}
                                                height={80}
                                                className="rounded-full border-2 border-gray-700"
                                            />
                                            <div className="pl-4">
                                                <h5 className="text-gray-100 font-semibold text-lg">Client Name</h5>
                                                <span className="text-sm uppercase tracking-[3px] text-gray-400">Profession</span>
                                            </div>
                                        </div>
                                    </div>
                                </SwiperSlide>
                            ))}
                        </Swiper>

                        {/* Navigation Buttons Below Image */}
                        <div className="flex space-x-4 mt-4">
                            <button
                                ref={prevRef}
                                className="w-12 h-12 bg-orange-500 text-white rounded-full flex items-center justify-center hover:bg-orange-400 transition-colors"
                                title="Previous testimonial"
                                aria-label="Previous testimonial"
                            >
                                <FaArrowLeft className="text-sm" />
                            </button>
                            <button
                                ref={nextRef}
                                className="w-12 h-12 bg-orange-500 text-white rounded-full flex items-center justify-center hover:bg-orange-400 transition-colors"
                                title="Next testimonial"
                                aria-label="Next testimonial"
                            >
                                <FaArrowRight className="text-sm" />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}
