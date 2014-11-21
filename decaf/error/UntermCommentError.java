package decaf.error;

import decaf.Location;

/**
 * example：unterminated string constant: "this is str"<br>
 * PA1
 */
public class UntermCommentError extends DecafError {
	
	public UntermCommentError(Location location) {
		super(location);
	}

	@Override
	protected String getErrMsg() {
		return "unterminated multi comment";
	}

}
