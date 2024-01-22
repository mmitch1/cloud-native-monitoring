function renderGauges(cpuPercent, memPercent) {
        var cpuGauge = {
            type: "indicator",
            mode: "gauge+number",
            value: cpuPercent,
            gauge: {
                axis: { range: [null, 100] },
                bar: { color: "#1f77b4"},
                bgcolor: "white",
                borderwidth: 2, 
                bordercolor: "#ccc",
                steps: [
                    { range: [0, 50], color: "#d9f0a3" },
                    { range: [50, 85], color: "#ffeb84" },
                    { range: [85, 100], color: "#ff5f5f" }
                ],
                threshold: {
                    line: { color: "red", width: 4 },
                    thickness: 0.75,
                    value: cpuPercent
                }
            }
        };

        var memGauge = {
            type: "indicator",
            mode: "gauge+number",
            value: memPercent,
            gauge: {
                axis: { range: [null, 100] },
                bar: { color: "#1f77b4"},
                bgcolor: "white",
                borderwidth: 2,
                bordercolor: "#ccc",
                steps: [
                    { range: [0, 50], color: "#d9f0a3" },
                    { range: [50, 85], color: "#ff3b84" },
                    { range: [ 85, 100], color: "#ff5f5f"}
                ],
                threshold: {
                    line: { color: "red", width: 4},
                    thickness: 0.75, 
                    value: memPercent
                }
            }
        };

        var cpuGaugeLayout = { title: "CPU Utilization" };
        var memGaugeLayout = { title: "Memory Utilization" };

        Plotly.newPlot('cpu-gauge', [cpuGauge], cpuGaugeLayout);
        Plotly.newPlot('mem-gauge', [memGauge], memGaugeLayout);
}