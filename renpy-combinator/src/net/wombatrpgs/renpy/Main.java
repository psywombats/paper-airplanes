/**
 *  Main.java
 *  Created on Jul 8, 2016 8:08:41 PM for project renpy-combinator
 *  Author: psy_wombats
 *  Contact: psy_wombats@wombatrpgs.net
 */
package net.wombatrpgs.renpy;

/**
 * Entry point.
 */
public class Main {
	
	private static String DEFAULT_INIT_FILENAME = "init.rpy";

	/**
	 * Entry point. Usage:
	 * 		args <dir> <out>
	 * 
	 * where <dir> is the top level directory of the folder to recursively build from, and <out> is
	 * the output file. Assumes there's a file called init.rpy located in the input directory at the
	 * top level, or else some file called initfile.
	 * 
	 * @param	args			Command line args: <dir> <out> [initfile]
	 */
	public static void main(String[] args) {
		if (args.length < 2 || args.length > 3) {
			System.out.println("Usage: renpy-combinator <dir> <our> [initfile]");
			return;
		}
		
		String initFilename;
		if (args.length == 3) {
			initFilename = args[2];
		} else {
			initFilename = DEFAULT_INIT_FILENAME;
		}
		
		System.out.println("Generating a script file from " + args[0] + " to " + args[1] + "...");
		CombinatorJob job = new CombinatorJob(args[0], args[1], initFilename);
		job.execute();
		System.out.println("Complete.");
	}

}
