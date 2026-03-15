import React, { useState } from 'react';

const App = () => {
  const [activePart, setActivePart] = useState(null);

  const components = [
    { id: 'core', name: 'Primary Carrier Core', color: '#3b82f6', info: 'Large superconducting solenoid that establishes the base phase frequency.' },
    { id: 'slaves', name: 'Gradient Slave Array', color: '#10b981', info: 'Hundreds of thin-film "fingerprint" coils wrapped around the core to steer the field.' },
    { id: 'resonators', name: 'Phase Resonators', color: '#f43f5e', info: 'Micro-coils that oscillate at THz frequencies to maintain the vacuum lock.' }
  ];

  return (
    <div className="flex flex-col h-screen bg-slate-950 text-slate-200 overflow-hidden font-sans">
      {/* Header */}
      <div className="p-4 border-b border-slate-800 bg-slate-900/50 flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-blue-400 tracking-widest uppercase italic">PDTP-V1 Cutaway Schematic</h1>
          <p className="text-xs text-slate-500">Internal Phase-Gradient Ring Architecture</p>
        </div>
        <div className="flex gap-2">
          {components.map(c => (
            <div key={c.id} className="flex items-center gap-2 px-3 py-1 bg-slate-800 rounded-full border border-slate-700 text-[10px]">
              <div className="w-2 h-2 rounded-full" style={{backgroundColor: c.color}}></div>
              {c.name}
            </div>
          ))}
        </div>
      </div>

      <div className="flex-1 grid grid-cols-12 gap-1 p-1">
        
        {/* LEFT: Full Craft View */}
        <div className="col-span-12 md:col-span-7 bg-slate-900/30 rounded-lg border border-slate-800 relative flex items-center justify-center overflow-hidden">
          <div className="absolute top-4 left-4 text-[10px] text-slate-500 font-mono uppercase tracking-widest">A. Operational Profile</div>
          
          <svg viewBox="0 0 500 300" className="w-full h-auto max-w-lg opacity-80">
            {/* Craft Outline */}
            <path d="M100,150 L200,80 L400,150 L200,220 Z" fill="none" stroke="#475569" strokeWidth="2" />
            <path d="M200,80 L220,130 L400,150" fill="none" stroke="#475569" strokeWidth="1" />
            
            {/* The Ring (Highlighted) */}
            <ellipse cx="230" cy="150" rx="40" ry="80" fill="none" stroke="#3b82f6" strokeWidth="6" strokeDasharray="4 2" />
            <ellipse cx="230" cy="150" rx="38" ry="78" fill="none" stroke="#60a5fa" strokeWidth="1" />
            
            {/* Field Visualization */}
            <path d="M230,70 C350,20 450,150 230,230" fill="none" stroke="#3b82f6" strokeWidth="1" opacity="0.3">
              <animate attributeName="stroke-dashoffset" from="100" to="0" dur="3s" repeatCount="indefinite" />
            </path>
            
            {/* Callout Line to Cutaway */}
            <line x1="250" y1="90" x2="450" y2="40" stroke="#94a3b8" strokeWidth="1" strokeDasharray="2 2" />
          </svg>
          
          <div className="absolute bottom-4 right-4 text-[10px] text-blue-500 font-mono">STATUS: PHASE-LOCKED</div>
        </div>

        {/* RIGHT COLUMN: Nested Detail */}
        <div className="col-span-12 md:col-span-5 grid grid-rows-2 gap-1">
          
          {/* TOP RIGHT: 3D Ring Cutaway */}
          <div className="bg-slate-900/50 rounded-lg border border-slate-800 p-4 relative overflow-hidden group">
             <div className="absolute top-2 left-2 text-[10px] text-slate-500 font-mono">B. 3D SECTION DETAIL (TOP-RIGHT)</div>
             
             <svg viewBox="0 0 300 200" className="w-full h-full">
                {/* 3D Torus Section */}
                <g transform="rotate(-15 150 100)">
                  {/* Outer Shield (Cut) */}
                  <path d="M50,100 A100,50 0 0,1 250,100" fill="none" stroke="#334155" strokeWidth="40" />
                  
                  {/* Inside layers (The "X amount" of coils) */}
                  <path d="M60,100 A90,45 0 0,1 240,100" fill="none" stroke="#10b981" strokeWidth="25" strokeDasharray="2 1" />
                  
                  {/* Core */}
                  <path d="M70,100 A80,40 0 0,1 230,100" fill="none" stroke="#3b82f6" strokeWidth="15" />
                  
                  {/* Cut-face detail */}
                  <ellipse cx="245" cy="100" rx="10" ry="20" fill="#1e293b" stroke="#64748b" strokeWidth="2" />
                  <ellipse cx="245" cy="100" rx="7" ry="14" fill="#064e3b" stroke="#10b981" strokeWidth="1" />
                  <ellipse cx="245" cy="100" rx="4" ry="8" fill="#1e3a8a" stroke="#3b82f6" strokeWidth="1" />
                </g>

                {/* Annotation */}
                <circle cx="245" cy="100" r="3" fill="white" />
                <line x1="245" y1="100" x2="180" y2="40" stroke="white" strokeWidth="0.5" />
                <text x="100" y="30" fill="white" fontSize="8" className="font-mono">CRYOGENIC VOID</text>
             </svg>
          </div>

          {/* BOTTOM RIGHT: Detail of the "X amount" of coils */}
          <div className="bg-slate-900 rounded-lg border border-slate-700 p-4 relative">
             <div className="absolute top-2 left-2 text-[10px] text-slate-500 font-mono">C. COIL DENSITY DETAIL</div>
             
             <div className="mt-4 grid grid-cols-2 gap-4 h-full">
                <div className="border border-slate-800 rounded bg-black/40 p-2 flex items-center justify-center overflow-hidden">
                   {/* Illustrating many coils around the one */}
                   <svg viewBox="0 0 100 100" className="w-full h-full">
                      <circle cx="50" cy="50" r="15" fill="none" stroke="#3b82f6" strokeWidth="4" />
                      {[...Array(24)].map((_, i) => (
                        <rect 
                          key={i}
                          x="48" y="10" width="4" height="15" 
                          fill="#10b981" 
                          transform={`rotate(${i * 15} 50 50)`} 
                          className="animate-pulse"
                          style={{ animationDelay: `${i * 0.1}s` }}
                        />
                      ))}
                   </svg>
                </div>
                <div className="text-[10px] space-y-2 text-slate-400">
                   <p className="text-white font-bold">The "Slave" Array:</p>
                   <p>Unlike standard motors, the PDTP uses <span className="text-emerald-400">discrete phase-cells</span>.</p>
                   <p>Each small green rectangle represents an independent coil segment. By varying the timing between them, we can "pulse" the phase field in a circle.</p>
                   <p className="italic text-slate-600">Total Segments: 1,024 per ring</p>
                </div>
             </div>
          </div>

        </div>
      </div>
      
      {/* Footer Info */}
      <div className="p-2 bg-blue-900/20 text-[10px] text-center text-blue-300 font-mono">
        WARNING: UNALIGNED PHASES MAY CAUSE INSTANT MASS REGAIN. ALWAYS SYNC REFERENCE OSCILLATOR BEFORE DECOUPLING.
      </div>
    </div>
  );
};

export default App;