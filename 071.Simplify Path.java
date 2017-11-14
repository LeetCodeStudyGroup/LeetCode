 /*
    Given an absolute path for a file (Unix-style), simplify it.

    For example,
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"
    path = "/home/foo/.ssh/../.ssh2/authorized_keys/" => "/home/foo/.ssh2/authorized_keys"
     */

    public String simplifyPath(String path) {
        if (path.equalsIgnoreCase("/"))
            return path;
        String output = "";
        String[] paths = path.split("/");
        Stack<String> stack = new Stack<>();
        for (int i=0; i<paths.length; i++) {
            if (paths[i].equalsIgnoreCase(".") || paths[i].isEmpty())
                continue;
            if (paths[i].equalsIgnoreCase("..")) {
                if (!stack.isEmpty())
                    stack.pop();
            } else {
                stack.push(paths[i]);
            }
        }

        for (String temp: stack) {
            if (!temp.isEmpty())
                output = output + "/" + temp;
        }

        if (output.isEmpty())
            output = "/";

        return output;
    }
