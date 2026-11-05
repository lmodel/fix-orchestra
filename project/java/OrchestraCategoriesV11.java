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
  The categories a repository sorts its messages and fields into.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraCategoriesV11  {

  private List<OrchestraCategoryV11> fixrCategory;
  private OrchestraAnnotationV11 fixrAnnotation;
  private URI xmlBase;


}