import os
import json
from graph import build_mom_graph

def main(video_path):
    graph = build_mom_graph()
    result = graph.invoke({"video_path": video_path})

    mom = result["MoM"]

    # Save to output file
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = f"data/outputs/{base_name}_mom.json"

    with open(output_path, "w") as f:
        json.dump({"MoM": mom}, f, indent=4)

    print(f"✅ MoM Generated and saved to: {output_path}")
    print("\n📝 Summary:\n", mom)

if __name__ == "__main__":
    main("data/meetings/meeting1.mp4")
