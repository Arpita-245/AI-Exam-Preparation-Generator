import Button from "../components/common/Button";
import Card from "../components/common/Card";

import Navbar from "../components/home/Navbar";
import Hero from "../components/home/Hero";
import Features from "../components/home/Features";
import HowItWorks from "../components/home/HowItWorks";
import Statistics from "../components/home/Statistics";
import Testimonials from "../components/home/Testimonials";
import FAQ from "../components/home/FAQ";
import CTA from "../components/home/CTA";
import Footer from "../components/common/Footer";

function Home() {
  return (
    <>
      <Navbar />

      <Hero />

      <Features />

      <HowItWorks />

      <Statistics />

      <Testimonials />

      <FAQ />

      {/* Temporary Design System Demo */}
      <section className="max-w-6xl mx-auto px-6 py-16">
        <Card>
          <h2 className="text-3xl font-bold mb-4">
            🎉 Design System Ready
          </h2>

          <p className="text-gray-600 mb-6">
            Your reusable UI components are working correctly.
            These components will be used throughout the project.
          </p>

          <div className="flex flex-wrap gap-4">
            <Button>Primary Button</Button>

            <Button variant="secondary">
              Secondary
            </Button>

            <Button variant="outline">
              Outline
            </Button>

            <Button variant="success">
              Success
            </Button>

            <Button variant="danger">
              Danger
            </Button>
          </div>
        </Card>
      </section>

      <CTA />

      <Footer />
    </>
  );
}

export default Home;