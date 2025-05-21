'use client'

import Image from 'next/image'

const blogPosts = [
    {
        image: '/images/menu-3.jpg',
        date: { day: '01', month: 'January', year: '2045' },
        title: 'Sed amet tempor amet sit kasd sea lorem',
    },
    {
        image: '/images/menu-5.jpg',
        date: { day: '01', month: 'January', year: '2045' },
        title: 'Sed amet tempor amet sit kasd sea lorem',
    },
    {
        image: '/images/menu-7.jpg',
        date: { day: '01', month: 'January', year: '2045' },
        title: 'Sed amet tempor amet sit kasd sea lorem',
    },
]

export default function Blog() {
    return (
        <section className="bg-white py-20 px-6">
            {/* Section Heading */}
            <div className="text-center max-w-3xl mx-auto mb-12">
                <h5 className="text-orange-500 uppercase tracking-[0.2em] font-medium mb-3">Our Blog</h5>
                <h2 className="text-4xl lg:text-5xl font-bold text-gray-800">Latest Articles From Food Blog</h2>
            </div>

            {/* Blog Cards */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                {blogPosts.map((post, index) => (
                    <div
                        key={index}
                        className="blog-item rounded-md shadow-md overflow-hidden bg-black group"
                    >
                        {/* Image with hover scale */}
                        <div className="overflow-hidden rounded-t-md">
                            <Image
                                src={post.image}
                                alt="Blog"
                                width={800}
                                height={500}
                                className="w-full h-64 object-cover transition-transform duration-500 group-hover:scale-110"
                            />
                        </div>

                        {/* Content */}
                        <div className="flex items-center p-5 text-white bg-zinc-900 rounded-b-md">
                            {/* Date Box */}
                            <div className="text-center text-gray-400 border-r border-gray-600 pr-4 mr-4 min-w-[60px]">
                                <p className="text-lg font-bold text-white leading-none">{post.date.day}</p>
                                <p className="uppercase text-orange-500 text-sm font-semibold leading-tight">
                                    {post.date.month}
                                </p>
                                <p className="text-sm leading-none">{post.date.year}</p>
                            </div>

                            {/* Title */}
                            <a href="#" className="text-white text-base font-semibold hover:underline">
                                {post.title}
                            </a>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    )
}
