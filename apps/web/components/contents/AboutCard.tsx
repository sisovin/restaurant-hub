'use client'
import React, { useEffect } from "react"
import Image from "next/image"
import { handleStickyNav, handleBackToTop, handleTeamHover } from "@/lib/animation"
import styles from "./AboutCard.module.css"

export default function AboutCard() {

    useEffect(() => {
        handleStickyNav()
        handleBackToTop()
        handleTeamHover()
    }, [])

    return (
        <>
            {/* About Start */}
            <div className="container-fluid p-5">
                <div className={`col-lg-5 mb-5 mb-lg-0 ${styles.aboutMinHeight}`}>
                    <div className={`col-lg-5 mb-5 mb-lg-0 ${styles.aboutImageContainer}`}>
                        <div className={`position-absolute top-0 start-0 animate-rotate ${styles.animateRotate}`}>
                            <div className={`position-absolute top-0 start-0 animate-rotate ${styles.aboutRoundImage}`}>
                                <Image
                                    className="img-fluid"
                                    src="/images/about-round.jpg"
                                    alt="About Round"
                                    width={160}
                                    height={160}
                                />
                            </div>
                            <div className="position-relative h-100 w-100">
                                <Image
                                    className="position-absolute w-100 h-100 rounded-circle rounded-bottom rounded-end"
                                    src="/images/about.jpg"
                                    alt="About"
                                    fill
                                    style={{ objectFit: "cover" }}
                                />
                            </div>
                        </div>
                    </div>
                    <div className="col-lg-7">
                        <div className="mb-4">
                            <h5 className="section-title font-body">About Us</h5>
                            <h1 className="display-3 mb-0 font-heading">Cooking Together With The Expert</h1>
                        </div>
                        <p className="mb-4 font-body">Nonumy erat diam duo labore clita. Sit magna ipsum dolor sed ea duo at ut. Tempor sit
                            lorem sit magna ipsum duo. Sit eos dolor ut sea rebum, diam sea rebum lorem kasd ut ipsum dolor est
                            ipsum. Et stet amet justo amet clita erat, ipsum sed at ipsum eirmod labore lorem.</p>
                        <div className="row">
                            <div className="col-sm-6">
                                <div className="bg-light rounded p-4">
                                    <div className="d-flex align-items-center mb-3">
                                        <Image
                                            className="img-fluid bg-primary rounded-circle"
                                            src="/images/feature-1.png"
                                            alt="Feature"
                                            width={80}
                                            height={80}
                                        />
                                    </div>
                                    <h4 className="font-body">Master Chefs</h4>
                                    <p className="mb-0 font-body">Tempor erat elitr at rebum at at clita aliquyam consetetur. Diam dolor diam
                                        ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing
                                        labore.</p>
                                </div>
                            </div>
                            <div className="col-sm-6">
                                <div className="bg-light rounded p-4">
                                    <div className="d-flex align-items-center mb-3">
                                        <Image
                                            className="img-fluid bg-primary rounded-circle"
                                            src="/images/feature-3.png"
                                            alt="Feature"
                                            width={80}
                                            height={80}
                                        />
                                    </div>
                                    <h4 className="font-body">Quality Food</h4>
                                    <p className="mb-0 font-body">Tempor erat elitr at rebum at at clita aliquyam consetetur. Diam dolor diam
                                        ipsum et, tempor voluptua sit consetetur sit. Aliquyam diam amet diam et eos sadipscing
                                        labore.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {/* About End */}
        </>
    )
}