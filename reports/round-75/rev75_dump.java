// revenger r75 capability demonstration postScript (Java, Ghidra 12.1.4 headless).
// Writes, for the imported program: image base, function count, and every
// function's decompiled C (or an explicit per-function failure marker).
// Output path comes from the REV75_OUT environment variable.
import ghidra.app.script.GhidraScript;
import ghidra.app.decompiler.DecompileOptions;
import ghidra.app.decompiler.DecompileResults;
import ghidra.app.decompiler.DecompInterface;
import ghidra.program.model.listing.Function;
import ghidra.program.model.listing.FunctionIterator;
import ghidra.program.model.listing.Program;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

public class rev75_dump extends GhidraScript {
	@Override
	public void run() throws Exception {
		String outPath = System.getenv("REV75_OUT");
		if (outPath == null || outPath.isEmpty()) {
			throw new IllegalStateException("REV75_OUT not set");
		}
		Program prog = currentProgram;
		DecompInterface di = new DecompInterface();
		di.setOptions(new DecompileOptions());
		di.openProgram(prog);
		FunctionIterator it = prog.getFunctionManager().getFunctions(true);
		List<Function> funcs = new ArrayList<>();
		while (it.hasNext()) {
			funcs.add(it.next());
		}
		int ok = 0;
		PrintWriter fh = new PrintWriter(new BufferedWriter(new FileWriter(outPath)));
		try {
			fh.println("program_name=" + prog.getName());
			fh.println("image_base=" + prog.getImageBase());
			fh.println("function_count=" + funcs.size());
			for (Function f : funcs) {
				DecompileResults res = di.decompileFunction(f, 120, monitor);
				fh.println("// ==== FUNC " + f.getName() + " @ " + f.getEntryPoint() + " ====");
				if (res != null && res.decompileCompleted()) {
					ok++;
					fh.println(res.getDecompiledFunction().getC());
				} else {
					fh.println("// DECOMPILE_FAILED");
				}
				fh.println();
			}
			fh.println("// decompiled_ok=" + ok + " of " + funcs.size());
		} finally {
			fh.close();
		}
		println("REV75_DUMP wrote " + outPath + ": " + funcs.size() + " functions, " + ok + " decompiled");
	}
}
