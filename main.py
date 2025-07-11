import sys
from dotenv import load_dotenv
load_dotenv()

from workflow.research_workflow import run_research_workflow

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "deep learning for cancer detection"

    print(f"Running research assistant with query: '{query}'")
    final_report = run_research_workflow(query)
    print("\n=== FINAL RESEARCH REPORT ===\n")
    print(final_report)

