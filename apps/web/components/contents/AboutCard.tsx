'use client';

import Image from 'next/image';

export default function AboutSection() {
    return (
        <section className="container-fluid px-5 py-12 lg:py-16">
            <div className="flex flex-col lg:flex-row gap-8 lg:gap-12">
                {/* Left Column - Image Section */}
                <div className="lg:w-5/12 mb-8 lg:mb-0 relative min-h-[500px]">
                    <div className="relative h-full">
                        {/* Create container with dark curved left edge */}
                        <div className="relative h-full w-full overflow-hidden">
                            {/* Main image */}
                            <div className="absolute left-[30px] right-0 top-0 bottom-0">
                                <div className="relative w-full h-full">
                                    <Image
                                        src="/images/about.jpg"
                                        alt="Chef cooking"
                                        fill
                                        className="object-cover rounded-tl-[50%]"
                                    />
                                </div>
                            </div>
                            {/* Rotating circular image - exactly positioned as in template */}
                            <div className="absolute top-1 left-1 animate-rotate w-[160px] h-[160px] z-20">
                                <Image
                                    src="/images/about-round.jpg"
                                    alt="Chef circular photo"
                                    width={160}
                                    height={160}
                                    className="w-full h-full rounded-full shadow-lg"
                                />
                            </div>
                        </div>
                    </div>
                </div>

                {/* Right Column - Text Content */}
                <div className="lg:w-7/12">
                    <div className="mb-6">
                        <h5 className="section-title text-orange-500 uppercase font-bold text-sm tracking-widest mb-2">About Us</h5>
                        <h1 className="text-4xl lg:text-5xl font-bold mb-2">Cooking Together With The Expert</h1>
                    </div>

                    <p className="text-gray-600 dark:text-gray-200 mb-6">
                        Nonumy erat diam duo labore clita. Sit magna ipsum dolor sed ea duo at ut. Tempor sit
                        lorem sit magna ipsum duo. Sit eos dolor ut sea rebum, diam sea rebum lorem kasd ut ipsum dolor est
                        ipsum. Et stet amet justo amet clita erat, ipsum sed at ipsum eirmod labore lorem.
                    </p>

                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">                        {/* Feature Box 1 */}
                        <div className="bg-gray-100 dark:bg-gray-600 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
                            <div className="bg-orange-500 rounded-full p-3 w-[80px] h-[80px] mb-4 flex items-center justify-center">
                                <Image
                                    src="/images/feature-1.png"
                                    alt="Master Chefs"
                                    width={50}
                                    height={50}
                                    className="object-contain"
                                />
                            </div>
                            <h4 className="text-xl font-semibold mb-2">Master Chefs</h4>
                            <p className="text-gray-600 dark:text-gray-200 text-sm">
                                Tempor erat elitr at rebum at at clita aliquyam consetetur. Diam dolor diam
                                ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing
                                labore.
                            </p>
                        </div>

                        {/* Feature Box 2 */}
                        <div className="bg-gray-100 dark:bg-gray-600 p-6 rounded-lg shadow-sm hover:shadow-md transition-shadow">
                            <div className="bg-orange-500 rounded-full p-3 w-[80px] h-[80px] mb-4 flex items-center justify-center">
                                <Image
                                    src="/images/feature-3.png"
                                    alt="Quality Food"
                                    width={50}
                                    height={50}
                                    className="object-contain"
                                />
                            </div>
                            <h4 className="text-xl font-semibold mb-2">Quality Food</h4>
                            <p className="text-gray-600 dark:text-gray-200 text-sm">
                                Tempor erat elitr at rebum at at clita aliquyam consetetur. Diam dolor diam
                                ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing
                                labore.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
}
