import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */ 
  allowedDevOrigins: [
    "http://localhost:3000",
    "http://192.168.1.108:3000",
    "http://192.168.50.131:3000"
  ]
};

export default nextConfig;
