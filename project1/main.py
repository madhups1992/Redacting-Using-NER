import argparse
import re

import project1

def main(files,otherfile,concept,outfile,statfile):
    Directory = '/project/cs5293sp19-project1/project1'
    file_regexp = '.txt'
    if (re.findall(file_regexp,files)):
        print("in if")
        filename , ls =project1.read_textfiles_from_directory(Directory, file_regexp)
        redacted_file=[]
        stats=[]
        concept = 'thank'
        for i in range(len(ls)):
            redacted_file.append(project1.redaction(ls[i],concept))
            stats.append(project1.redation_summary(ls[i],concept))
        project1.store_redactedfiles(redacted_file,Directory,filename)
        project1.Writing_statistics(stats,Directory+'/'+statfile+'.txt',filename)

    else:
        print("Mismatch type")


if __name__ == '__main__':
    print("in main")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",type=str,required=True)
    parser.add_argument("--names",type=str,required=False)
    parser.add_argument("--date",type=str,required=False)
    parser.add_argument("--addresses",type=str,required=False)
    parser.add_argument("--phones",type=str,required=False)
    parser.add_argument("--concept",type=str,required=True)
    parser.add_argument("--output",type=str,required=True)
    parser.add_argument("--stats",type=str,required=False)

    args = []
    args= parser.parse_args()
    if args.input:
        files = args.input
    if args.concept:
        concept = args.concept
    if args.output:
        outfile = args.output
        otherfile=args.output
    if args.stats:
        statfile = args.stats
    main(files,otherfile,concept,outfile,statfile)


else:
    print("in else")
