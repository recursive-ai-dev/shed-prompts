Act as a Senior Machine Learning Engineer and review this Jupyter Notebook (.ipynb) for production readiness and execution integrity. Search specifically for:

    Execution Order & Hidden State: Stale cell dependencies, non-sequential state reliance, or variables leaking across out-of-order execution runs.

    Data Pipeline Inefficiencies: Unbatched data loading, redundant pandas/numpy transforms, CPU-to-GPU data transfer bottlenecks, or memory leaks during training/inference loops.

    Model Artifact Safety: Unsaved checkpoints, missing random seed definitions for reproducibility, and unvalidated tensor shape transformations.

Clean up the notebook flow, optimize compute/memory usage, and provide clear step-by-step improvements to ensure the workflow is reproducible and ready for export to a clean python module.
