package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An encoding standard a repository uses, with a name to show and its general encoding information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraEncodingStandardV11  {

  private OrchestraUnnamedEncodingV11 fixrEncoding;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;
  private String fixrDisplayName;


}