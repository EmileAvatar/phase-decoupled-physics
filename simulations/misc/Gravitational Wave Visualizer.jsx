import React, { useState, useEffect, useRef } from 'react';

const App = () => {
  const [mode, setMode] = useState('plus'); // 'plus', 'cross', 'breathing'
  const [amplitude, setAmplitude] = useState(30);
  const requestRef = useRef();
  const timeRef = useRef(0);
  const canvasRef = useRef(null);

  const draw = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const centerX = width / 2;
    const centerY = height / 2;
    const t = timeRef.current;

    ctx.clearRect(0, 0, width, height);
    
    // Draw background grid
    ctx.strokeStyle = '#334155';
    ctx.lineWidth = 1;
    for (let i = 0; i < width; i += 40) {
      ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, height); ctx.stroke();
    }
    for (let i = 0; i < height; i += 40) {
      ctx.beginPath(); ctx.moveTo(0, i); ctx.lineTo(width, i); ctx.stroke();
    }

    // Grid of particles
    const rows = 12;
    const cols = 12;
    const spacing = 35;
    const startX = centerX - (cols * spacing) / 2 + spacing / 2;
    const startY = centerY - (rows * spacing) / 2 + spacing / 2;

    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        let x = startX + c * spacing;
        let y = startY + r * spacing;
        
        // Relative coordinates from center
        const dx = x - centerX;
        const dy = y - centerY;

        const phase = Math.sin(t);
        const shift = (amplitude * phase) / 100;

        let finalX = x;
        let finalY = y;

        if (mode === 'plus') {
          // Tensor Plus: Stretch X, Squeeze Y
          finalX += dx * shift;
          finalY -= dy * shift;
        } else if (mode === 'cross') {
          // Tensor Cross: Stretch/Squeeze Diagonals
          // This is a rotation of the plus mode
          const diag = (dx + dy) * 0.707;
          const antiDiag = (dx - dy) * 0.707;
          const shiftX = (diag * shift * 0.707) + (antiDiag * -shift * 0.707);
          const shiftY = (diag * shift * 0.707) - (antiDiag * -shift * 0.707);
          finalX += shiftX;
          finalY += shiftY;
        } else if (mode === 'breathing') {
          // Scalar Breathing: Uniform expansion/contraction
          finalX += dx * shift;
          finalY += dy * shift;
        }

        // Draw particle
        ctx.beginPath();
        ctx.arc(finalX, finalY, 4, 0, Math.PI * 2);
        ctx.fillStyle = mode === 'breathing' ? '#f43f5e' : '#3b82f6';
        ctx.fill();
      }
    }

    timeRef.current += 0.05;
    requestRef.current = requestAnimationFrame(draw);
  };

  useEffect(() => {
    requestRef.current = requestAnimationFrame(draw);
    return () => cancelAnimationFrame(requestRef.current);
  }, [mode, amplitude]);

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-slate-900 text-white p-8 font-sans">
      <div className="max-w-2xl w-full bg-slate-800 rounded-2xl shadow-2xl p-6 border border-slate-700">
        <h1 className="text-2xl font-bold mb-2 text-center text-blue-400">Gravitational Wave Modes</h1>
        <p className="text-slate-400 text-sm mb-6 text-center">
          Compare Einstein's Predicted Waves (Blue) with PDP's "Breathing" Wave (Red).
        </p>

        <div className="flex justify-center mb-8 bg-slate-900 rounded-xl p-2 border border-slate-700">
          <canvas 
            ref={canvasRef} 
            width={500} 
            height={500} 
            className="max-w-full h-auto rounded-lg"
          />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <button 
            onClick={() => setMode('plus')}
            className={`p-3 rounded-lg font-bold transition ${mode === 'plus' ? 'bg-blue-600 text-white' : 'bg-slate-700 hover:bg-slate-600'}`}
          >
            Tensor: Plus (+)
          </button>
          <button 
            onClick={() => setMode('cross')}
            className={`p-3 rounded-lg font-bold transition ${mode === 'cross' ? 'bg-blue-600 text-white' : 'bg-slate-700 hover:bg-slate-600'}`}
          >
            Tensor: Cross (×)
          </button>
          <button 
            onClick={() => setMode('breathing')}
            className={`p-3 rounded-lg font-bold transition ${mode === 'breathing' ? 'bg-rose-600 text-white' : 'bg-slate-700 hover:bg-slate-600'}`}
          >
            PDP: Breathing
          </button>
        </div>

        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium">Wave Amplitude</span>
            <input 
              type="range" 
              min="5" max="80" 
              value={amplitude} 
              onChange={(e) => setAmplitude(parseInt(e.target.value))}
              className="w-2/3 h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer"
            />
          </div>

          <div className="p-4 bg-slate-900/50 rounded-xl border border-slate-700/50 text-sm leading-relaxed">
            {mode === 'plus' && "Einstein's Standard: Stretches vertically while squeezing horizontally."}
            {mode === 'cross' && "Einstein's Standard: Same as Plus, but rotated 45 degrees."}
            {mode === 'breathing' && "The PDTP Prediction: Everything expands and contracts together. This is a signature of a scalar phase field."}
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;