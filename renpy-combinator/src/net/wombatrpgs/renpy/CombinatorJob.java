/**
 *  CombinatorJob.java
 *  Created on Jul 8, 2016 8:13:09 PM for project renpy-combinator
 *  Author: psy_wombats
 *  Contact: psy_wombats@wombatrpgs.net
 */
package net.wombatrpgs.renpy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Excecutable class for recombining renpy files.
 */
public class CombinatorJob {
	
	protected static String DISCLAIMER_MESSAGE = "# WARNING! This file is generated! Do not edit!";
	
	protected String inDirectoryFilename;
	protected String outFilename;
	protected String initFilename;
	
	/**
	 * Creates (but does not run) a new job.
	 * @param	inDirectoryFilename	The name of the directory to recursively read from
	 * @param	outFilename			The name of the file to write to
	 * @param	initFilename		The name of the file with initialization code (should be first)
	 */
	public CombinatorJob(String inDirectoryFilename, String outFilename, String initFilename) {
		this.inDirectoryFilename = inDirectoryFilename;
		this.outFilename = outFilename;
		this.initFilename = initFilename;
	}
	
	/**
	 * Runs the combinator job and generates the output file!
	 */
	public void execute() {
		try {
			File outFile = new File(outFilename);
			outFile.createNewFile();
			BufferedWriter writer = new BufferedWriter(new FileWriter(outFile));
			
			writer.write(DISCLAIMER_MESSAGE + "\n\n");
			
			File initFile = new File(initFilename);
			BufferedReader initReader = new BufferedReader(new FileReader(initFile));
			cat(initReader, writer);
			
			for (File file : recursivelyListFiles(new File(inDirectoryFilename))) {
				// don't double-write init if it happens to be in the dir
				if (!file.getAbsolutePath().equals(initFile.getAbsolutePath())) {
					BufferedReader reader = new BufferedReader(new FileReader(file));
					cat(reader, writer);
				}
			}
			
			writer.close();
			
		} catch (IOException exception) {
			exception.printStackTrace();
			System.err.println("IO exception in job body");
		}
	}
	
	/**
	 * Recursively adds all files in the given directory to a list and returns it.
	 * @param	directory			The directory to read from
	 * @return						A list of all non-directory files in that directory and children
	 */
	protected List<File> recursivelyListFiles(File directory) {
		ArrayList<File> results = new ArrayList<>();
		for (File file : directory.listFiles()) {
			if (file.isDirectory()) {
				results.addAll(recursivelyListFiles(file));
			} else {
				results.add(file);
			}
		}
		return results;
	}
	
	/**
	 * Writes the contents of reader into writer. Does not open the streams or close them either.
	 * @param	reader				The reader to read from
	 * @param	writer				The writer to write to
	 */
	protected void cat(BufferedReader reader, BufferedWriter writer) throws IOException {
		while (reader.ready()) {
			writer.write(reader.readLine() + "\n");
		}
		writer.write("\n");
	}
}
