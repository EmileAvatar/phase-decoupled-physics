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
            <div 
              key={c.id} 
              onMouseEnter={() => setActivePart(c.id)}
              onMouseLeave={() => setActivePart(null)}
              className={`flex items-center gap-2 px-3 py-1 rounded-full border transition-all duration-300 text-[10px] cursor-help ${
                activePart === c.id ? 'bg-slate-700 border-white' : 'bg-slate-800 border-slate-700'
              }`}
            >
              <div className="w-2 h-2 rounded-full" style={{backgroundColor: c.color}}></div>
              {c.name}
            </div>
          ))}
        </div>
      </div>

      <div className="flex-1 grid grid-cols-12 gap-1 p-1 overflow-hidden">
        
        {/* LEFT: Full Craft View (Operational Profile) */}
        <div className="col-span-12 lg:col-span-5 bg-slate-900/30 rounded-lg border border-slate-800 relative flex flex-col items-center justify-center p-4">
          <div className="absolute top-4 left-4 text-[10px] text-slate-500 font-mono uppercase tracking-widest">A. Craft Profile</div>
          
          <svg viewBox="0 0 500 300" className="w-full h-auto opacity-80">
            {/* Craft Outline */}
            <path d="M100,150 L200,80 L400,150 L200,220 Z" fill="none" stroke="#475569" strokeWidth="2" />
            <path d="M200,80 L220,130 L400,150" fill="none" stroke="#475569" strokeWidth="1" />
            
            {/* The Ring (Highlighted) */}
            <ellipse cx="230" cy="150" rx="40" ry="80" fill="none" stroke="#3b82f6" strokeWidth={activePart === 'core' ? 8 : 4} strokeDasharray="4 2" />
            
            {/* Field Visualization */}
            <path d="M230,70 C350,20 450,150 230,230" fill="none" stroke="#3b82f6" strokeWidth="1" opacity="0.3">
              <animate attributeName="stroke-dashoffset" from="100" to="0" dur="3s" repeatCount="indefinite" />
            </path>
            
            {/* Callout Line to Cutaway */}
            <line x1="250" y1="90" x2="480" y2="50" stroke="#94a3b8" strokeWidth="1" strokeDasharray="5 5" />
          </svg>
          
          <div className="mt-4 p-3 bg-slate-900/80 rounded border border-slate-700 w-full">
            <h3 className="text-[10px] font-bold text-blue-400 mb-1">CRAFT STATUS</h3>
            <div className="flex justify-between text-[9px] font-mono">
              <span>COUPLING ($\alpha$):</span>
              <span className="text-emerald-400">0.042 (DECOUPLED)</span>
            </div>
          </div>
        </div>

        {/* RIGHT: Detailed Cutaway Section (The "Right Side" detail) */}
        <div className="col-span-12 lg:col-span-7 grid grid-rows-2 gap-1 overflow-hidden">
          
          {/* TOP RIGHT: 3D Ring Cutaway Section */}
          <div className="bg-slate-900/50 rounded-lg border border-slate-800 p-6 relative overflow-hidden group">
             <div className="absolute top-2 left-2 text-[10px] text-slate-500 font-mono">B. 3D RING SEGMENT CUTAWAY</div>
             
             <div className="flex h-full items-center">
               <svg viewBox="0 0 400 250" className="flex-1 h-full drop-shadow-2xl">
                  <g transform="translate(50, 50) rotate(-10)">
                    {/* Outer Casing (Cut) */}
                    <path d="M0,80 A150,60 0 0,1 300,80" fill="none" stroke="#1e293b" strokeWidth="60" strokeLinecap="round" />
                    <path d="M0,80 A150,60 0 0,1 300,80" fill="none" stroke="#334155" strokeWidth="56" strokeLinecap="round" />
                    
                    {/* Slave Coil Layer (The "X amount" surrounding the core) */}
                    <path 
                      d="M20,80 A130,50 0 0,1 280,80" 
                      fill="none" 
                      stroke={activePart === 'slaves' ? '#10b981' : '#064e3b'} 
                      strokeWidth="35" 
                      strokeDasharray="2 2" 
                      className="transition-colors duration-300"
                    />
                    
                    {/* Main Carrier Core */}
                    <path 
                      d="M40,80 A110,40 0 0,1 260,80" 
                      fill="none" 
                      stroke={activePart === 'core' ? '#60a5fa' : '#1e3a8a'} 
                      strokeWidth="15" 
                      className="transition-colors duration-300"
                    />

                    {/* End-Cap Face (The Cross-Section) */}
                    <g transform="translate(300, 80)">
                      <ellipse cx="0" cy="0" rx="25" ry="40" fill="#0f172a" stroke="#475569" strokeWidth="2" />
                      <ellipse cx="0" cy="0" rx="18" ry="30" fill="none" stroke="#10b981" strokeWidth="4" strokeDasharray="2 1" />
                      <ellipse cx="0" cy="0" rx="8" ry="15" fill="#1e3a8a" stroke="#3b82f6" strokeWidth="2" />
                    </g>
                  </g>

                  {/* Annotations */}
                  <g className="text-[10px] font-mono">
                    <line x1="330" y1="110" x2="360" y2="80" stroke="#94a3b8" />
                    <text x="365" y="80" fill="#3b82f6">SUPERCONDUCTING CORE</text>
                    
                    <line x1="315" y1="130" x2="360" y2="150" stroke="#94a3b8" />
                    <text x="365" y="155" fill="#10b981">GRADIENT SLAVE WRAP</text>
                  </g>
               </svg>
               
               <div className="w-1/3 p-4 bg-black/40 rounded border border-slate-800 text-[10px] space-y-3">
                 <h4 className="text-white font-bold border-b border-slate-700 pb-1">INTERNAL Vitals</h4>
                 <p><span className="text-blue-400">Core Temp:</span> 4.2K</p>
                 <p><span className="text-emerald-400">Slave Density:</span> 1024/m</p>
                 <p><span className="text-rose-400">Sync Tolerance:</span> &lt;1ps</p>
               </div>
             </div>
          </div>

          {/* BOTTOM RIGHT: Detail of the "X amount" of coils (Slave Array) */}
          <div className="bg-slate-900 rounded-lg border border-slate-700 p-6 relative overflow-hidden">
             <div className="absolute top-2 left-2 text-[10px] text-slate-500 font-mono uppercase">C. Slave Array "Fingerprint" Detail</div>
             
             <div className="flex gap-8 h-full items-center">
                {/* Visual of coils wrapping around */}
                <div className="w-1/2 h-full bg-black/60 rounded-xl border border-slate-800 flex items-center justify-center p-2 relative">
                   <svg viewBox="0 0 200 120" className="w-full h-full">
                      {/* Main pipe represention */}
                      <rect x="20" y="40" width="160" height="40" rx="20" fill="#1e3a8a" opacity="0.4" />
                      
                      {/* The wrapping "X amount" of coils */}
                      {[...Array(15)].map((_, i) => (
                        <path 
                          key={i}
                          d={`M ${30 + i * 10} 35 Q ${35 + i * 10} 20, ${40 + i * 10} 35 L ${40 + i * 10} 85 Q ${35 + i * 10} 100, ${30 + i * 10} 85 Z`}
                          fill="none" 
                          stroke="#10b981" 
                          strokeWidth="1.5"
                          opacity={0.8}
                        >
                          <animate 
                            attributeName="stroke-opacity" 
                            values="0.3;1;0.3" 
                            dur="2s" 
                            begin={`${i * 0.1}s`} 
                            repeatCount="indefinite" 
                          />
                        </path>
                      ))}
                      
                      <text x="100" y="65" textAnchor="middle" fill="#60a5fa" fontSize="6" className="font-bold">PRIMARY CARRIER CORE</text>
                   </svg>
                   <div className="absolute bottom-2 text-[8px] text-emerald-500 font-mono">DENSITY: 128 CHANNELS PER SEGMENT</div>
                </div>

                {/* Explanation text */}
                <div className="flex-1 space-y-4">
                   <div className="bg-slate-800/50 p-3 rounded border border-slate-700">
                     <h3 className="text-emerald-400 text-xs font-bold uppercase mb-1">The "X Amount" Breakdown</h3>
                     <p className="text-[10px] leading-relaxed text-slate-300">
                       Wrapping the **Primary Carrier Core** is an array of "Slave" coils. Unlike the main core which provides the static phase, these segments are addressed individually by the **Phase-Controlled Coil Drivers**.
                     </p>
                   </div>
                   
                   <ul className="text-[10px] space-y-2 text-slate-400">
                     <li className="flex gap-2">
                       <span className="text-emerald-500">▶</span>
                       <span><strong>Inductive Steering:</strong> By pulsing these slaves in sequence, we shift the center of the phase-lock.</span>
                     </li>
                     <li className="flex gap-2">
                       <span className="text-emerald-500">▶</span>
                       <span><strong>Resonant Coupling:</strong> These coils vibrate the local vacuum to create the "Acoustic Metric" slope.</span>
                     </li>
                   </ul>
                </div>
             </div>
          </div>

        </div>
      </div>
      
      {/* Footer / Safety Warning */}
      <div className="p-2 bg-rose-950/30 text-[9px] text-center text-rose-400 font-mono border-t border-rose-900/50">
        CRITICAL: ENSURE CRYOGENIC TEMPERATURES BEFORE ENERGIZING PRIMARY CORE. PHASE SLIPPAGE MAY RESULT IN LOCALIZED SPATIOTEMPORAL SHEAR.
      </div>
    </div>
  );
};

export default App;